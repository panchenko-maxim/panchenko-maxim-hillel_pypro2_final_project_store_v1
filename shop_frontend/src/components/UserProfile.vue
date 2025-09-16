<template>
  <div class="container mt-4">
    <h2>User Profile: {{ username }}</h2>
    <!-- Здесь можно отобразить данные пользователя -->
  </div>
</template>

<script>
export default {
  name: 'UserProfile',
  computed: {
    username() {
        return this.$route.params.username
    }
  }
//   mounted() {
//     // const username = this.$route.params.username;
//     // Здесь можно сделать запрос к Django API: /api/users/:username
//   }
}
</script>