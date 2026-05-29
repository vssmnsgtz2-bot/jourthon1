document.addEventListener('DOMContentLoaded', function(){
  const nav = document.querySelector('.site-nav');
  const hamburger = document.querySelector('.nav-hamburger');
  const menu = document.querySelector('.mobile-menu');
  const onScroll = () => nav && nav.classList.toggle('scrolled', window.scrollY > 40);
  onScroll(); window.addEventListener('scroll', onScroll);
  if (hamburger && menu) {
    hamburger.addEventListener('click', () => { hamburger.classList.toggle('open'); menu.classList.toggle('open'); document.body.style.overflow = menu.classList.contains('open') ? 'hidden' : ''; });
    menu.querySelectorAll('a').forEach(a => a.addEventListener('click', () => { hamburger.classList.remove('open'); menu.classList.remove('open'); document.body.style.overflow = ''; }));
  }
  const reveals = document.querySelectorAll('.reveal');
  const observer = new IntersectionObserver((entries)=>{ entries.forEach(e=>{ if(e.isIntersecting){ e.target.classList.add('visible'); observer.unobserve(e.target); } }); }, {threshold:.1, rootMargin:'0px 0px -40px 0px'});
  reveals.forEach(el=>observer.observe(el));
});