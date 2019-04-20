// Page scroll
window.pageYOffset;
window.scrollTo(0, 0);


// Element scroll (read or write)
el.scrollTop
el.scrollLeft


// Element width/height (includes padding and border)
el.getBoundingClientRect().width;
el.getBoundingClientRect().height;


// Body width/height excluding window scrollbars
document.body.getBoundingClientRect().width;
document.body.getBoundingClientRect().height;


// Window width/height including scrollbars
window.innerWidth;
window.innerHeight;


// Position relative to viewport
el.getBoundingClientRect().top;
el.getBoundingClientRect().left;
el.getBoundingClientRect().bottom;
el.getBoundingClientRect().right;


// Position relative to offset parent
el.offsetLeft;
el.offsetTop;


// Styles
el.style.zIndex = 1;
el.style.removeProperty('z-index');
getComputedStyle(el).zIndex;


// Classes
el.classList.add('test');
el.classList.remove('test');
el.classList.contains('test');
$(el).toggleClass('test'); // IE doesn't support classList.toggle


// DOM
var div = document.createElement('div');

el.appendChild(div);
el.removeChild(div);
el.insertBefore(div, el.firstChild);

el.parentNode;
el.children;

el.setAttribute('tabindex', 3);
el.getAttribute('tabindex');
el.removeAttribute('tabindex');

el.innerHTML = '<p>Test</p>';
el.textContent = 'Test';


// Query
document.querySelector('.test');
document.querySelectorAll('.test');
document.getElementById('test');

el.querySelector('.test');
el.querySelectorAll('.test');


// Arrays
xs.indexOf(x);


// Strings
s.trim();


// Location hash
window.location.hash.substr(1);


// Regex match
/^te/.test('test');


// Dispatch events
el.click();
el.dispatchEvent(new Event('change'));
