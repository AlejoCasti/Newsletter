<template lang="pug">
div
  .loader
  .spinner
</template>
<style scoped>
.loader {
  position: fixed;
  top: 0;
  bottom: 0;
  left: 0;
  right: 0;
  background: rgba(0, 0, 0, 0.7);
  transition: opacity 350ms;
  opacity: 0.9;
  z-index: 999;
}

.spinner {
  position: fixed;
  top: 50%;
  right: 50%;
  border: 4px solid rgba(0, 0, 0, 0.1);
  width: 36px;
  height: 36px;
  border-radius: 50%;
  border-left-color: #00D180;
  animation: spin 1s ease infinite;
  z-index: 9999;
}

@keyframes spin {
  0% {
    transform: rotate(0deg);
  }

  100% {
    transform: rotate(360deg);
  }
}
</style>