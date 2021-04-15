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

async function loadMutations() {
  setPeriod();

  var data = await fetchApi(API.wallet.name);
  initFromNames(data);
  initMaterials();

  data = await fetchApi(API.mutation.get);
  mutationData = data;
  generateTable();

  showTable();
  showForm();
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
