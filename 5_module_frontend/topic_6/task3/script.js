const taskElem = document.getElementById("taskInput");
const tasksListElem = document.getElementById("tasks");

var tasks = [];
var taskCount = 1;

function handleDelete() {
  console.log("test");
}

function handleClick() {
  tasksListElem.innerHTML += `
  <li>
    ${taskElem.value}
    <button
        id="delete-task-${taskCount}" 
        style="background-color: red"
        onclick="${handleDelete()}"
    >
        x
    </button>
  </li>
   `;
  taskElem.value = "";
  taskCount += 1;
}
