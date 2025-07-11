function searchWord() {
    const query = document.getElementById('searchInput').value;
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
            data.forEach(item => {
                const li = document.createElement('li');
                li.textContent = item.text + ' - ' + item.language.code;
                list.appendChild(li);
            });
            results.appendChild(list);
        });
}
