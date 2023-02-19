$(document).ready(function () {
  // Зчитування стану collapse елементів при завантаженні сторінки
  restoreCollapseState();

  // Збереження стану collapse елементів при зміні стану
  $(".collapse").on("hidden.bs.collapse shown.bs.collapse", function () {
    setCollapseState($(this).attr("id"), $(this).hasClass("show"));
  });
});

// Збереження стану collapse елементів у локальному сховищі браузера
function setCollapseState(id, state) {
  localStorage.setItem(id, state);
}

// Зчитування стану collapse елементів з локального сховища браузера
function restoreCollapseState() {
  $(".collapse").each(function () {
    var id = $(this).attr("id");
    var state = localStorage.getItem(id);
    if (state === "true") {
      $(this).addClass("show");
    }
  });
}
