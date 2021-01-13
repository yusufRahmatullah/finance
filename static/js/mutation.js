function generateTable(mutations) {
  var tableNode = q('#table-body');
  var ctn = '';

  mutations.forEach(m => {
    ctn += mutationView(m);
  });

  appendNode(tableNode, ctn);
}

function loadMutations() {
  fetch('/mutations/get')
  .then(resp => resp.json())
  .then(data => {
    setPeriod();
    generateTable(data);
  })
  .catch(err => {
    console.error("Failed get mutations. " + err);
  })
}

function mutationView(m, bold) {
  var tr_attr = '';
  if (bold) {
    tr_attr = 'class="bold"';
  }

  return `
  <tr ${tr_attr}>
    <td>${m.date}</td>
    <td>${m.thing}</td>
    <td>${humanizeName(m.from)}</td>
    <td>${humanizeName(m.to)}</td>
    <td>${humanizeAmount(m.amount)}</td>
    <td>${humanizeAmount(m.from_left)}</td>
  </tr>
  `;
}
