document.addEventListener("DOMContentLoaded", function() {
  const stars = document.querySelectorAll('.user-rating .star');
  const input = document.getElementById('rating-input');
  const form = document.getElementById('rating-form');

  stars.forEach(star => {
    star.addEventListener('mouseenter', () => {
      const val = star.dataset.value;
      highlightStars(val);
    });

    star.addEventListener('mouseleave', () => {
      resetStars();
    });

    star.addEventListener('click', () => {
      const val = star.dataset.value;
      input.value = val;
      form.submit();
    });
  });

  function highlightStars(val) {
    stars.forEach(s => {
      if (s.dataset.value <= val) s.classList.add('filled');
      else s.classList.remove('filled');
    });
  }

  function resetStars() {
    const currentVal = input.value;
    stars.forEach(s => {
      if (s.dataset.value <= currentVal) s.classList.add('filled');
      else s.classList.remove('filled');
    });
  }
});
