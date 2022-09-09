const SCRIPT_ROOT = "{{ request.script_root|tojson }}"
console.log(SCRIPT_ROOT)


fetch("http://", {
    method: 'POST',
    headers: {
        'Accept': 'text/xml',
        'Content-Type': 'application/json'
    },
    body: JSON.stringify({
        
    }).then(response => response.text())
    .then(r => console.log(r))


})