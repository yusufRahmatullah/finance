const API = {
  summary: 'summary',
  budget: {
    get: '/budgets/get',
    name: '/budgets/names',
    total: '/budgets/total',
  },
  mutation: {
    get: '/mutations/get',
  },
  transaction: {
    get: '/transactions/get',
  },
  wallet: {
    get: '/wallets/get',
    name: '/wallets/names',
  },
};

async function fetchApi(api) {
  try {
    var resp = await fetch(api);
    var data = await resp.json();
  } catch (e) {
    console.log(`Failed fetch Api ${api}`);
    data = {};
  } finally {
    return data;
  }
}
