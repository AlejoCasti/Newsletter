<template lang="pug">
.dashboard-container
  .header
    router-link.back-icon(to="/")
      i.material-symbols-outlined arrow_back

    h3 Dashboard

  .simple-data-container
    section(style="background-color: #00D180")
      i.material-symbols-outlined.data-icon forward_to_inbox
      .data-container
        span.secondary-text-section Total emails sent
        span.primary-text-section {{ totalEmailsSent }}
    section(style="background-color: #45f1af")
      i.material-symbols-outlined.data-icon group
      .data-container
        span.secondary-text-section Total active users
        span.primary-text-section {{ totalActiveUsers }}
    section(style="background-color: #0e6242")
      i.material-symbols-outlined.data-icon group_remove
      .data-container
        span.secondary-text-section Total unsubscriptions
        span.primary-text-section {{ totalUnsubscriptions }}
    section(style="background-color: #519a7e")
      i.material-symbols-outlined.data-icon clock_loader_90
      .data-container
        span.secondary-text-section Unsubscription rate
        span.primary-text-section {{ `${unsubscriptionRate}%` }}
</template>
<script>
import apiService from '../services/Api/apiController';

export default {
  name: 'DashboardPage',
  data() {
    return {
      totalEmailsSent: 0,
      totalActiveUsers: 0,
      totalUnsubscriptions: 0,
      unsubscriptionRate: 0,
    }
  },
  async mounted() {
    try {
      const { data } = await apiService.getStatistics();
      this.totalEmailsSent = data.total_emails_sent
      this.totalActiveUsers = data.total_active_users
      this.totalUnsubscriptions = data.total_unsubscriptions
      this.unsubscriptionRate = data.unsubscription_rate
    } catch (e) {
      if (e.response && e.response.status === 401) return;
      Swal.fire({
        title: 'Error!',
        text: 'An error occurred during the process. Please try again later.',
        icon: 'error',
        confirmButtonColor: '#00D180',
        confirmButtonText: 'Continue',
      })
    }
  }
}
</script>
<style scoped>
.dashboard-container{
  background: white;
  padding: 40px 20px;
  border-radius: 10px;
  width: 700px;
  display: flex;
  flex-direction: column;
  gap: 20px;
}

.header {
  display: flex;
  align-items: center;
  gap: 10px;
}

.simple-data-container {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  justify-content: center;
  gap: 20px;
}

section {
  border-radius: 5px;
  width: 40%;
  height: 200px;
  display: flex;
  align-items: center;
  padding: 20px;
  color: white;
  gap: 10px;
}

.data-container {
  display: flex;
  flex-direction: column;
  align-items: start;
}

.primary-text-section {
  font-weight: bold;
}

.primary-text-section {
  font-weight: bold;
  font-size: 32px;
}

.secondary-text-section {
  font-size: 14px;
  font-style: italic;
}

.data-icon {
  color: white;
  font-size: 52px;
}

.back-icon {
  display: flex;
  align-items: center;
}
</style>