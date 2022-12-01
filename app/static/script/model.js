$(document).ready(function () {
  flatpickr("#date", {
    dateFormat: "Y-m-d",
    minDate: "today",
    defaultDate: "today",
  });

  flatpickr("#eDate", {
    dateFormat: "Y-m-d",
    minDate: "today",
    defaultDate: "today",
  });

  setTimeout(() => $(".alert").alert("close"), 4000);

  $(".status").click(function () {
    const status = $(this);
    const tID = status.data("id");
    let new_status;
    if (status.text() === "In Progress") {
      new_status = "Complete";
    } else if (status.text() === "Complete") {
      new_status = "Todo";
    } else if (status.text() === "Todo") {
      new_status = "In Progress";
    }

    $.ajax({
      type: "POST",
      url: "/status/" + tID,
      contentType: "application/json;charset=UTF-8",
      data: JSON.stringify({
        status: new_status,
      }),
      success: function (res) {
        console.log(res.response);
        location.reload();
      },
      error: function () {
        console.log("Error");
      },
    });
  });

  $("#sTask").click(function () {
    let date = document.getElementById("date").value;
    let description = document.getElementById("task-description").value;
    $.ajax({
      type: "POST",
      url: "/insert",
      contentType: "application/json;charset=UTF-8",
      data: JSON.stringify({
        date: date,
        description: description,
      }),
      success: function (res) {
        console.log(res.response);
        location.reload();
      },
      error: function () {
        console.log("Error");
      },
    });
  });

  $("#remove").on("click", function () {
    $("[data-toggle=confirmation]").confirmation({
      rootSelector: "[data-toggle=confirmation]",
    });
  });

  deleteTask = (ID) => {
    let result = confirm("Are you sure you want to delete this task?");
    let id = parseInt(ID);
    if (!result) {
      e.preventDefault();
    } else {
      $.ajax({
        type: "POST",
        url: "/remove/" + id,
        contentType: "application/json;charset=UTF-8",
        data: JSON.stringify({
          ID: id,
        }),
        success: function (res) {
          console.log(res.response);
          location.reload();
        },
        error: function () {
          console.log("Error");
        },
      });
    }
  };
});
