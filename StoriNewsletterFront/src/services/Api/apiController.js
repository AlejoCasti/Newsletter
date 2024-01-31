import conn from './index';

export default {
  login({ username, password }) {
    return conn.post('/auth/login/', { username, password });
  },
  signUp({ username, password }) {
    return conn.post('/auth/register/', { username, password });
  },
  logout() {
    return conn.post('/auth/logout/');
  },
  createNewsletter({ title, emails, fileName }) {
    return conn.post('/newsletter/create/', {
      title,
      recipients_emails: emails,
      source_name: fileName,
    });
  },
  deleteNewsletter({ id }) {
    return conn.delete(`/newsletter/delete/${id}/`);
  },
  getNewsletters() {
    return conn.get('/newsletter/list/');
  },
  sendEmail({ id }) {
    return conn.post('newsletter/send/', {
      id,
    });
  },
  unsubscribe({ token }) {
    return conn.get(`newsletter/unsubscribe/${token}`);
  },
  getStatistics() {
    return conn.get('/newsletter/statistics/');
  },
};
