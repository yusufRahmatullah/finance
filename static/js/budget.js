function budgetView(budget) {
  return `
  <tr>
    <td>${budget.name}</td>
    <td>${humanizeAmount(budget.amount)}</td>
    <td>${humanizeAmount(budget.left)}</td>
  </tr> 
  `
}

function generateTable(budgets) {
  var tableNode = q('#table-body');
  var ctn = '';

  budgets.forEach(b => {
    ctn += budgetView(b);
  });
  appendNode(tableNode, ctn);
}

function getBudgets() {
  fetch('/budgets/get')
    .then(resp => resp.json())
    .then(data => {
      setPeriod();
      generateTable(data);
    })
    .catch(err => {
      console.error("Failed get budgets. " + err);
    })
}
