  document.getElementById('register').addEventListener('click', function() {
    document.getElementById('my-hidden-input').value = 'register';
    document.getElementById('my-form').submit();
  });
  
  document.getElementById('login').addEventListener('click', function() {
    document.getElementById('my-hidden-input').value = 'login';
    document.getElementById('my-form').submit();
  });

