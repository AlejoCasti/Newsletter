<template lang="pug">
.dropzone-container
  label.dropzone-label(v-if="!url") Upload file here
    input(type="file" @change="handleFileUpload" accept="image/png, application/pdf")

  .file-preview(v-else)
    i.material-symbols-outlined.delete-icon(@click="deleteImage") cancel
    img(v-if="file.type === 'image/png'" :src="url" width="250")
    template(v-else)
      img(src="https://upload.wikimedia.org/wikipedia/commons/thumb/8/87/PDF_file_icon.svg/1280px-PDF_file_icon.svg.png" width="50")
      span {{ file.name }}

</template>
<script>
import Swal from 'sweetalert2'

export default {
  name: 'Dropzone',
  props: ['formFile'],
  data() {
    return {
      file: null,
      url: null,
    };
  },
  watch: {
    formFile(newValue) {
      if (!newValue) {
        this.file = null;
        this.url = null;
      }
    },
  },
  methods: {
    handleFileUpload(e) {
      const fileSize = e.target.files[0].size;
      const sizeInKb = Math.round(fileSize / 1024);

      if (sizeInKb > 10240) {
        Swal.fire({
          title: 'Error!',
          text: 'The file exceeds the allowed size (10MB)',
          icon: 'error',
          confirmButtonColor: '#00D180',
          confirmButtonText: 'Continue',
        })
        e.target.value = '';
        return;
      }
      this.file = e.target.files[0];
      this.url = URL.createObjectURL(this.file);

      this.$emit('onUpload', this.file);
    },
    deleteImage() {
      this.file = null;
      this.url = null;
      this.$emit('onDelete');
    },
  },
};
</script>
<style scoped>
.dropzone-container {
  width: inherit;
}

.dropzone-label {
  border: 1px dashed #ccc;
  padding: 6px 12px;
  cursor: pointer;
  box-sizing: border-box;
  display: block;
}

input[type='file'] {
  display: none;
}

.file-preview {
  border: 1px dashed #ccc;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-direction: column;
  gap: 15px;
  padding: 10px;
}

.delete-icon {
  color: rgb(253, 110, 110);
  font-size: 22px;
  align-self: flex-end;
}
</style>
