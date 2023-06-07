window.onscroll = () => {
  const nav = document.querySelector('#navbar');
  if(this.scrollY <= 10) nav.className = ''; else nav.className = 'scroll';

    const div = document.querySelector('#RichFeyn');
  if(this.scrollY <= 10) div.className = ''; else div.className = 'scroll';
};

