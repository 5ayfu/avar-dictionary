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
    fetch(`/api/dictionary/search/?q=${encodeURIComponent(query)}`)
        .then(res => res.json())
        .then(updateResults);
}

// Legacy API used by some handlers
function searchWord() {
    const query = document.getElementById('searchInput').value.trim();
    fetchWords(query);
}
