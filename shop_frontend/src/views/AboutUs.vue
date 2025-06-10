<template>
  <div class="about-us-page">
    <h1>About Us</h1>
    <p>Welcome to our "About Us" page! We are a team of passionate individuals dedicated to creating innovative solutions for your business.</p>
    <p>Our mission is to deliver high-quality products and services that help our clients achieve their goals and thrive in today's dynamic digital world.</p>

    <div class="team-section">
      <h2>Our Team</h2>
      <div class="team-member">
        <img src="https://img.freepik.com/premium-photo/angry-mad-face-asian-man-blue-t-shirt-isolated-space_39688-3946.jpg" alt="Team Member 1 Photo" class="team-photo">
        <h3>John Doe</h3>
        <p>Co-founder & CEO</p>
        <p>John has over 15 years of experience in software development and strategic planning, driving our vision forward.</p>
      </div>
      <div class="team-member">
        <img src="https://cdn.mos.cms.futurecdn.net/v2/t:127,l:0,cw:800,ch:450,q:80,w:800/DMUbjq2UjJcG3umGv3Qjjd.jpeg" alt="Team Member 2 Photo" class="team-photo">
        <h3>Jane Smith</h3>
        <p>Lead Designer</p>
        <p>Jane specializes in creating intuitive and beautiful user interfaces, paying meticulous attention to every detail.</p>
      </div>
      <div class="team-member">
        <img src="https://st.depositphotos.com/1776223/2032/i/950/depositphotos_20322059-stock-photo-angry-face-of-a-man.jpg" alt="Team Member 3 Photo" class="team-photo">
        <h3>Mike Johnson</h3>
        <p>Head of Marketing</p>
        <p>Mike is an expert in digital marketing, ensuring our products reach the right audience and make an impact.</p>
      </div>
    </div>

    <p>Feel free to contact us to learn more about how we can help you!</p>
  </div>
</template>

<script>
export default {
  name: 'AboutUsPage', 
};
</script>

<style scoped>
.about-us-page {
  max-width: 960px;
  margin: 40px auto;
  padding: 20px;
  background-color: #fff;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
  border-radius: 8px;
  line-height: 1.6;
  color: #333;
}

h1 {
  text-align: center;
  color: #2c3e50;
  margin-bottom: 30px;
}

h2 {
  text-align: center;
  color: #34495e;
  margin-top: 40px;
  margin-bottom: 25px;
}

p {
  margin-bottom: 15px;
  text-align: justify;
}

.team-section {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 30px;
  margin-top: 40px;
}

.team-member {
  text-align: center;
  flex: 0 0 calc(33% - 40px); 
  min-width: 250px; 
  background-color: #f9f9f9;
  padding: 20px;
  border-radius: 8px;
  box-shadow: 0 1px 5px rgba(0, 0, 0, 0.05);
}

.team-photo {
  width: 120px;
  height: 120px;
  border-radius: 50%;
  object-fit: cover;
  margin-bottom: 15px;
  border: 3px solid #42b983; 
}

.team-member h3 {
  color: #2c3e50;
  margin-bottom: 5px;
}

.team-member p {
  font-size: 0.9em;
  color: #666;
}

@media (max-width: 768px) {
  .team-member {
    flex: 0 0 calc(50% - 30px); 
  }
}

@media (max-width: 480px) {
  .team-member {
    flex: 0 0 100%; 
  }
}
</style>