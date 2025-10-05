// Handle dictionary page interactions
function fetchWordDetails(id) {
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
            if (data.translations && data.translations.length) {
                const tTitle = document.createElement('h3');
                tTitle.textContent = 'Translations';
                container.appendChild(tTitle);
                const ul = document.createElement('ul');
                data.translations.forEach(t => {
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
    const results = document.getElementById('results');
    const details = document.getElementById('wordDetails');
    let fromLang = 'av';
    let toLang = 'en';
    if (toggle) {
        toggle.textContent = `${fromLang}→${toLang}`;
    }

    async function quickTranslate(word) {
        if (!word) {
            if (results) {
                results.innerHTML = '';
            }
            if (details) {
                details.innerHTML = '';
            }
            return;
        }
        const url = `/api/dictionary/translate/?word=${encodeURIComponent(word)}&from=${fromLang}&to=${toLang}`;
        const res = await fetch(url);
        const data = await res.json();
        if (!results) {
            return;
        }
        results.innerHTML = '';
        if (!Array.isArray(data) || !data.length) {
            results.textContent = 'No translations';
            return;
        }
        const list = document.createElement('ul');
        list.className = 'results-list';
        data.forEach(t => {
            const li = document.createElement('li');
            const fromText = `${t.from_word.text} (${t.from_word.language.code})`;
            const toText = `${t.to_word.text} (${t.to_word.language.code})`;
            li.textContent = `${fromText} → ${toText}`;
            li.dataset.id = t.to_word.id;
            list.appendChild(li);
        });
        results.appendChild(list);
    }

    if (toggle) {
        toggle.addEventListener('click', () => {
            [fromLang, toLang] = [toLang, fromLang];
            toggle.textContent = `${fromLang}→${toLang}`;
            if (input) {
                quickTranslate(input.value.trim());
            }
        });
    }

    const triggerSearch = () => {
        if (input) {
            quickTranslate(input.value.trim());
        }
    };

    if (form) {
        form.addEventListener('submit', (e) => {
            e.preventDefault();
            triggerSearch();
        });
    }

    if (input) {
        input.addEventListener('input', triggerSearch);
    }

    if (results) {
        results.addEventListener('click', (e) => {
            if (e.target.tagName === 'LI') {
                fetchWordDetails(e.target.dataset.id);
            }
        });
    }

    const params = new URLSearchParams(window.location.search);
    if (input && params.has('q')) {
        input.value = params.get('q');
        triggerSearch();
    }
});
