document.getElementById('warm-up-btn').addEventListener('click', function() {
    document.getElementById('warm-up-modal').style.display = 'block';
});

document.getElementById('warm-up-close-btn').addEventListener('click', function() {
    document.getElementById('warm-up-modal').style.display = 'none';
});

document.getElementById('open-report').addEventListener('click', function() {
    window.location.href = '/report/';
});

document.getElementById('openModalBtn').addEventListener('click', function() {
    document.getElementById('myModal').style.display = 'block';
});

document.getElementById('closeModalBtn').addEventListener('click', function() {
    document.getElementById('myModal').style.display = 'none';
});

document.getElementById('smtp-imap').addEventListener('click', function() {
    document.getElementById('SMTPModal').style.display = 'block';
});

document.getElementById('SMTPcloseModalBtn').addEventListener('click', function() {
    document.getElementById('SMTPModal').style.display = 'none';
});

window.addEventListener('click', function(event) {
    if (event.target === document.getElementById('myModal')) {
        document.getElementById('myModal').style.display = 'none';
    }
    if (event.target === document.getElementById('SMTPModal')) {
        document.getElementById('SMTPModal').style.display = 'none';
    }
});
