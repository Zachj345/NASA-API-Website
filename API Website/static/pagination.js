  // PAGINATION

  const Items = document.querySelector(".pictures").children;
  const prev = document.querySelector(".prev");
  const next = document.querySelector(".next");
  const page = document.querySelector(".page-number");
  const maxItem = 24;
  let index = 1;

  const pagination = Math.ceil(Items.length / maxItem);
  console.log(pagination);

  prev.addEventListener("click", function () {
    index--;
    check();
    showItems();
  });

  next.addEventListener("click", function () {
    index++;
    check();
    showItems();
  });

  function check() {
    if (index == pagination) {
      next.classList.add("disabled");
    } else {
      next.classList.remove("disabled");
    }
    if (index == 1) {
      prev.classList.add("disabled");
    } else {
      prev.classList.remove("disabled");
    }
  }

  function showItems() {
    for (let i = 0; i < Items.length; i++) {
      Items[i].classList.remove("show");
      Items[i].classList.add("hide");
      if (i >= index * maxItem - maxItem && i < index * maxItem) {
        Items[i].classList.remove("hide");
        Items[i].classList.add("show");
      }
    }
    page.innerHTML = "Page #" + index;
  }

  window.onload = function () {
    showItems();
    check();
  };

