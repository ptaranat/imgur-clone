<template>
  <div class="login-box center-align">
    <h4>Confirm Signup</h4>
    <div class="card-panel red darken-2" v-if="error != null">
      <span class="white-text">{{ error.message }}</span>
    </div>
    <p>Enter the verification code you should have recieved via email</p>
    <form class="form-group">
      <div class="input-field">
        <label for="username">Username</label>
        <input
          id="username"
          type="text"
          class="form-control"
          v-model="username"
          required
        />
      </div>
      <div class="input-field">
        <label for="confirmcode">Confirmation Code</label>
        <input
          id="confirmcode"
          type="text"
          class="form-control"
          v-model="confirmcode"
          required
        />
      </div>
      <div class="center-align">
        <br />
        <button v-on:click="confirm()" class="btn btn-danger btn-large">
          Verify Now
        </button>
      </div>
    </form>
  </div>
</template>

<script>
export default {
  name: "Confirm",
  data() {
    return {
      username: "",
      confirmcode: "",
      error: null,
    };
  },
  methods: {
    confirm() {
      /*eslint no-unused-vars: "off"*/
      this.$cognitoAuth.confirmRegistration(
        this.username,
        this.confirmcode,
        (err, result) => {
          if (err) {
            this.error = err;
          } else {
            this.$router.push("/profile");
          }
        }
      );
    },
  },
};
//confirmcode
</script>

<style scoped>
h4 {
  text-align: center;
  margin: 0;
  padding: 0;
  font-weight: 400;
  font-size: 18px;
}
p {
  text-align: center;
  font-size: 14px;
  padding-bottom: 10px;
}
.login-box {
  width: 400px;
  height: auto;
  color: #d1d2d2;
  background-color: #343a40;
  border-radius: 5px;
  padding: 40px;
  margin: auto;
  margin-top: 60px;
  box-shadow: 0px 2px 5px rgba(0, 0, 0, 0.4);
}
button {
  margin: auto;
  margin: 0;
  padding: 0px 40px;
}
button i {
  font-size: 18px;
}
</style>