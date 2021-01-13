function budgetView(budget, bold) {
  var tr_attr = '';
  if (bold) {
    tr_attr = 'class="bold"';
  }

  return `
  <tr ${tr_attr}>
    <td>${humanizeName(budget.name)}</td>
    <td>${humanizeAmount(budget.amount)}</td>
    <td>${humanizeAmount(budget.left)}</td>
  </tr>
  `;
}

function generateTable(budgets) {
  var tableNode = q('#table-body');
  var ctn = '';
  var total = 0;
  var total_left = 0;

  budgets.forEach(b => {
    ctn += budgetView(b);
    total += b.amount;
    total_left += b.left;
  });
  ctn += budgetView({
    name: 'Total',
    amount: total,
    left: total_left,
  }, true);

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
