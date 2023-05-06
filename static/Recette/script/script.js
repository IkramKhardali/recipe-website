const ratingForm = document.getElementById('rating-form');

  if (document.querySelector('.messages .success')) {
      ratingForm.querySelectorAll('input').forEach(function (input) {
          input.disabled = true;
      });

      ratingForm.querySelector('button[type="submit"]').disabled = true;
  }