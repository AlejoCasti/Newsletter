<template lang="pug">
.newsletter-list-container
  DataTable(v-if="newsletters.length > 0" :value="newsletters" tableStyle="max-width: 50rem")
    column(field="title" header="Title")
    column(field="recipients_emails" header="Emails")
    column(field="source_name" header="Source name")
    column(header="Send")
      template(#body="slotProps")
        i.material-symbols-outlined(@click="() => onSendClick(slotProps.data.id)") send
    
    column(header="Delete")
      template(#body="slotProps")
        i.material-symbols-outlined(@click="() => onDeleteNewsletter(slotProps.data.id)") delete
  
  span(v-else) You don't have newspapers yet, create one.
</template>
<script>
import DataTable from 'primevue/datatable';
import Column from 'primevue/column';

export default {
  name: 'NewsletterList',
  components: { DataTable, Column },
  props: ['newsletters'],
  methods: {
    onSendClick(id) {
      this.$emit('onSendClick', id);
    },
    onDeleteNewsletter(id) {
      this.$emit('onDeleteNewsletter', id);
    }
  },
};
</script>
<style scoped>
</style>
