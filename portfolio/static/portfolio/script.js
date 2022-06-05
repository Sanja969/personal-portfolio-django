const projects = document.querySelectorAll('.project');
const blogs = document.querySelectorAll('.blog');

for (let i = 0; i < projects.length; i += 1) {
  projects[i].style.backgroundColor = "rgb(" +
  Math.floor(Math.random() * 100) +
  ", " +
  Math.floor(Math.random() * 100) +
  ", " +
  Math.floor(Math.random() * 100) +
  ", 0.4)";
}

for (let i = 0; i < blogs.length; i += 1) {

  blogs[i].style.backgroundColor = "rgb(" +
  Math.floor(Math.random() * 100) +
  ", " +
  Math.floor(Math.random() * 100) +
  ", " +
  Math.floor(Math.random() * 100) +
  ", 0.4)";
}



