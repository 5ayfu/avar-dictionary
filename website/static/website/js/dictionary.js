// Handle dictionary page interactions
function fetchWordDetails(id, toLang) {
    fetch(`/api/dictionary/words/${id}/`)
        .then(res => res.json())
        .then(data => {
            const container = document.getElementById('wordDetails');
            container.innerHTML = '';
            const title = document.createElement('h2');
            title.textContent = data.text;
            container.appendChild(title);
            if (data.transcription) {
                const tr = document.createElement('p');
                tr.textContent = data.transcription;
                container.appendChild(tr);
            }
            const translations = (data.translations || []).filter(t => t.to_word.language.code === toLang);
            if (translations.length) {
                const tTitle = document.createElement('h3');
                tTitle.textContent = 'Translations';
                container.appendChild(tTitle);
                const ul = document.createElement('ul');
                translations.forEach(t => {
                    const li = document.createElement('li');
                    li.textContent = `${t.to_word.text} - ${t.to_word.language.code}`;
                    ul.appendChild(li);
                });
                container.appendChild(ul);
            }
            if (data.examples && data.examples.length) {
                const eTitle = document.createElement('h3');
                eTitle.textContent = 'Examples';
                container.appendChild(eTitle);
                const ul = document.createElement('ul');
                data.examples.forEach(ex => {
                    const li = document.createElement('li');
                    li.textContent = ex.translation ? `${ex.text} - ${ex.translation}` : ex.text;
                    ul.appendChild(li);
                });
                container.appendChild(ul);
            }
        });
}

document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('searchForm');
    const input = document.getElementById('searchInput');
    const toggle = document.getElementById('directionToggle');
    let fromLang = 'av';
    let toLang = 'en';
    if (toggle) {
        toggle.textContent = `${fromLang}→${toLang}`;
        toggle.addEventListener('click', () => {
            [fromLang, toLang] = [toLang, fromLang];
            toggle.textContent = `${fromLang}→${toLang}`;
            fetchWords(input.value.trim());
        });
    }

    function updateResults(data) {
        const results = document.getElementById('results');
        results.innerHTML = '';
        if (!data || data.length === 0) {
            results.innerHTML = '<p>No results</p>';
            return;
        }
        const list = document.createElement('ul');
        list.className = 'results-list';
        data.forEach(item => {
            const li = document.createElement('li');
            li.textContent = item.text + ' - ' + item.language.code;
            li.dataset.id = item.id;
            list.appendChild(li);
        });
        results.appendChild(list);
    }

    function fetchWords(query = '') {
        const url = `/api/dictionary/search/?q=${encodeURIComponent(query)}&language=${fromLang}`;
        fetch(url)
            .then(res => res.json())
            .then(updateResults);
    }

    if (form) {
        form.addEventListener('submit', (e) => {
            e.preventDefault();
            fetchWords(input.value.trim());
        });
    }
    if (input) {
        input.addEventListener('input', () => {
            fetchWords(input.value.trim());
        });
        fetchWords('');
    }
    document.getElementById('results').addEventListener('click', (e) => {
        if (e.target.tagName === 'LI') {
            fetchWordDetails(e.target.dataset.id, toLang);
        }
    });
});
