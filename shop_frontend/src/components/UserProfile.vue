<template>
  <div class="container mt-4">
    <h2>User Profile: {{ username }}</h2>
    <h2>Userdata: {{  userData }}</h2>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'UserProfile',  
  data() {
    return {
        username: '',
        userData: null,
        errorMessage: '',
        loading: true,
    };
  },
  mounted() {
    this.username = this.$route.params.username;
    this.fetchUserData();
  },
  methods: {
    async fetchUserData(){
        try {
            const response = await axios.get(`http://localhost:8000/api/users/${this.username}/`);
            this.userData = response.data
        } catch (error) {
            if (error.response) {
                this.errorMessage = `Error ${error.response.status}: ${error.response.data.detail} || 'Failed to retrieve user data.'`
            } else if (error.request) {
                this.errorMessage = 'The server is not responding. Check your connection.'
            } else {
                this.errorMessage = 'Error response: ' + error.message;
            }
        } finally {
            this.loading = false;
        }
    }
  }
 
}
</script>