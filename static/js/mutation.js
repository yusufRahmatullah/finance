/* Mutation function flow
  loadMutations (fetch /wallets/names)  ->  initFromNames
                                            initMaterials
                                            getMutations (fetch /mutations/get) ->  generateTable -> (each) mutationView
*/

var mutationData = [];

function generateTable() {
  var tableNode = q('#table-body');
  var ctn = '';
  var from_name = q('#from-options').value;

  tableNode.innerHTML = '';

  mutationData.forEach(m => {
    if (from_name == 'all' || from_name == m.from) {
      ctn += mutationView(m);
    }
  });

  appendNode(tableNode, ctn);
}

function getMutations() {
  setPeriod();

  fetch('/mutations/get')
  .then(resp => resp.json())
  .then(data => {
    mutationData = data;
    generateTable();
  })
  .catch(err => {
    console.error("Failed get mutations. " + err);
  })
}

function initFromNames(names) {
  var node = q('#from-options');
  var ctn = '';

  names.forEach(name => {
    var from_name = humanizeName(name);
    ctn += `<option value="${name}">${from_name}</option>`
  });

  appendNode(node, ctn);
}

function initMaterials() {
  // select
  var elems = document.querySelectorAll('select');
  var instances = M.FormSelect.init(elems);
}

function loadMutations() {
  // get wallet names first
  fetch('/wallets/names')
  .then(resp => resp.json())
  .then(data => {
    initFromNames(data);
    initMaterials();
    getMutations();
  })
  .catch(err => {
    console.error("Failed load wallets. " + err);
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
