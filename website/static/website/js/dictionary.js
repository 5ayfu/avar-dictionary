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
    if (form) {
        form.addEventListener('submit', (e) => {
            e.preventDefault();
            searchWord();
        });
    }
    if (input) {
        input.addEventListener('input', () => {
            fetchWords(input.value.trim());
        });
        // initial list when page loads
        fetchWords('');
    }
    document.getElementById('results').addEventListener('click', (e) => {
        if (e.target.tagName === 'LI') {
            fetchWordDetails(e.target.dataset.id);
        }
    });
});
