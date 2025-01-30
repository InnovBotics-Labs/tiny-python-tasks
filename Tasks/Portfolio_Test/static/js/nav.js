    let currentActiveDiv = null;

    function showContent(id) {
      if (currentActiveDiv) {
        currentActiveDiv.classList.remove('active');
      }

      const targetDiv = document.getElementById(id);

      if (currentActiveDiv !== targetDiv) {
        targetDiv.classList.add('active');
        currentActiveDiv = targetDiv;
      } else {
        currentActiveDiv = null;
      }
    }