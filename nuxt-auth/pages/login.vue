<template>
    <div class="login-container">
      <h1>Login</h1>
      <form @submit.prevent="signUp">

        <div>
          <label for="email">Email</label>
          <input type="email" v-model="email" id="email" required>
        </div>
        <div>
          <label for="password">Senha</label>
          <input type="password" v-model="password" id="password" required>
        </div>
        <button type="submit">Registrar</button>
        <div v-if="errorMsg" class="error">{{ errorMsg }}</div>
        <div v-if="successMsg" class="success">{{ successMsg }}</div>
      </form>
    </div>
  </template>
  
  <script setup>
  import { ref } from 'vue'
  
  const client = useSupabaseClient().auth
  const email = ref("")
  const password = ref("")
  const errorMsg = ref("")
  const successMsg = ref("")
  
  async function signUp() {
    try {
      const { error } = await client.signUp({
        email: email.value,
        password: password.value
      })
      if (error) throw error
      successMsg.value = 'Verifique seu email para o link de login!'
    } catch (error) {
      errorMsg.value = error.message
    }
  }
  </script>
  
  <style scoped>
  .login-container {
    max-width: 400px;
    margin: 0 auto;
    padding: 20px;
    border: 1px solid #ccc;
    border-radius: 5px;
  }
  
  form div {
    margin-bottom: 15px;
  }
  
  label {
    display: block;
    margin-bottom: 5px;
  }
  
  input {
    width: 100%;
    padding: 8px;
    box-sizing: border-box;
  }
  
  button {
    width: 100%;
    padding: 10px;
    background-color: #007BFF;
    color: white;
    border: none;
    border-radius: 5px;
    cursor: pointer;
  }
  
  button:hover {
    background-color: #0056b3;
  }
  
  .error {
    color: red;
  }
  
  .success {
    color: green;
  }
  </style>
  