function searchWord() {
    const query = document.getElementById('searchInput').value.trim();
    if (!query) return;
    fetch(`/api/dictionary/search/?q=${encodeURIComponent(query)}`)
        .then(res => res.json())
        .then(data => {
            const results = document.getElementById('results');
            results.innerHTML = '';
            if (data.length === 0) {
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
        });
}
