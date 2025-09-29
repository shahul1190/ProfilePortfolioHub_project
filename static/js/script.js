

// Navigation Bar Toggle
const navbarToggle = document.querySelector('.navbar-toggler');
const navbarCollapse = document.querySelector('.navbar-collapse');

navbarToggle.addEventListener('click', () => {
  navbarCollapse.classList.toggle('show');
});

// Smooth Scrolling
const scrollLinks = document.querySelectorAll('a.scroll-link');

scrollLinks.forEach(link => {
  link.addEventListener('click', event => {
    event.preventDefault();
    const targetId = link.getAttribute('href');
    const targetElement = document.querySelector(targetId);
    targetElement.scrollIntoView({ behavior: 'smooth' });
  });
});

// Active Navigation Link
const navLinks = document.querySelectorAll('.nav-link');

navLinks.forEach(link => {
  link.addEventListener('click', () => {
    navLinks.forEach(l => l.classList.remove('active'));
    link.classList.add('active');
  });
});

// Scroll to Top Button
const scrollTopButton = document.querySelector('.scroll-top');

window.addEventListener('scroll', () => {
  if (window.scrollY > 500) {
    scrollTopButton.classList.add('show');
  } else {
    scrollTopButton.classList.remove('show');
  }
});

scrollTopButton.addEventListener('click', () => {
  window.scrollTo({ top: 0, behavior: 'smooth' });
});

// Auth App JavaScript
const loginForm = document.querySelector('#login-form');
const registerForm = document.querySelector('#register-form');

loginForm.addEventListener('submit', event => {
  event.preventDefault();
  const username = document.querySelector('#username').value;
  const password = document.querySelector('#password').value;
  // Login API call
});

registerForm.addEventListener('submit', event => {
  event.preventDefault();
  const username = document.querySelector('#username').value;
  const email = document.querySelector('#email').value;
  const password = document.querySelector('#password').value;
  // Register API call
});

// Portfolio App JavaScript
const projectForm = document.querySelector('#project-form');

projectForm.addEventListener('submit', event => {
  event.preventDefault();
  const title = document.querySelector('#title').value;
  const description = document.querySelector('#description').value;
  const image = document.querySelector('#image').value;
  const link = document.querySelector('#link').value;
  // Create Project API call
});

// Edit Project Form
const editProjectForm = document.querySelector('#edit-project-form');

editProjectForm.addEventListener('submit', event => {
  event.preventDefault();
  const title = document.querySelector('#title').value;
  const description = document.querySelector('#description').value;
  const image = document.querySelector('#image').value;
  const link = document.querySelector('#link').value;
  // Edit Project API call
});

// Ensure event listener is attached
document.getElementById('make-change-btn').addEventListener('click', function() {
    console.log('Button clicked');
});
