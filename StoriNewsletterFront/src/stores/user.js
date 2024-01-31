import { defineStore } from 'pinia';

export const useUserStore = defineStore('user', {
  state: () => ({
    newsletters: [],
  }),
  actions: {
    setNewsletters: ({ newsletters: [] }) => {
      this.newsletters = newsletters;
    },
  },
});
