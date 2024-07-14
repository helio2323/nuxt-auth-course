<template>
    <div>
        <h1>Login Page</h1>
        <div class="form">
            <BForm>
    <BFormControl margin="b-3">
      <BFormLabel>Email address</BFormLabel>
      <BFormInput
        v-model="email"
        type="email"
      />
      <BFormText>We'll never share your email with anyone else.</BFormText>
    </BFormControl>
    <BFormControl margin="b-3">
      <BFormLabel>Password</BFormLabel>
      <BFormInput
        v-model="password"
        type="password"
      />
    </BFormControl>
    <BFormCheck margin="b-3">
      <BFormCheckInput v-model="checked" />
      <BFormCheckLabel>Check me out</BFormCheckLabel>
    </BFormCheck>
    <b-button
      type="submit"
      button="primary"
      @click="requestOptions"
    >
      Submit
    </b-button>
  </BForm>
  <b-dl margin="t-2">
    <b-dt col="sm-3">
      Email
    </b-dt>
    <b-dd col="sm-9">
      {{ email }}
    </b-dd>
    <b-dt col="sm-3">
      Password
    </b-dt>
    <b-dd col="sm-9">
      <span>{{ password }}</span>
    </b-dd>
    <b-dt col="sm-3">
      Checked
    </b-dt>
    <b-dd col="sm-9">
      {{ checked }}
    </b-dd>
  </b-dl>
        </div>
    </div>
</template>

<script setup>

const email = ref('')
const password = ref('')
const checked = ref(false)

const requestOptions = {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({
    email: email.value,
    password: password.value
  })
}

fetch('/api/login', requestOptions)
  .then(response => response.json())
  .then(data => console.log(data))


</script>

<style scoped>

div {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
}

.form {
    display: flex;
    flex-direction: column;
    gap: 20px;
    justify-content: start;
    padding: 30px;
    align-items: start;
    background-color: #DDD;
}

</style>