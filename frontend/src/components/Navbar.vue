<template>
  <b-navbar toggleable="lg" type="dark" variant="dark">
    <b-navbar-brand href="/">Image Repo</b-navbar-brand>
    <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>
    <b-collapse id="nav-collapse" is-nav>
      <b-navbar-nav>
        <b-nav-item v-if="isLoggedIn()">
          <router-link class="nav-link" to="profile">Profile</router-link>
        </b-nav-item>
        <b-nav-item v-if="isLoggedIn()">
          <router-link class="nav-link" to="upload">Upload</router-link>
        </b-nav-item>
        <b-nav-item v-if="!isLoggedIn()">
          <router-link class="nav-link" to="login">Login</router-link>
        </b-nav-item>
        <b-nav-item v-if="!isLoggedIn()">
          <router-link class="nav-link" to="register">Register</router-link>
        </b-nav-item>
      </b-navbar-nav>

      <b-navbar-nav class="ml-auto">
        <b-nav-form>
          <b-form-input
            size="sm"
            class="mr-sm-2"
            placeholder="Search (WIP)"
          ></b-form-input>
          <b-button size="sm" class="my-2 my-sm-0" type="submit"
            >Search</b-button
          >
        </b-nav-form>
        <b-nav-item-dropdown
          v-if="isLoggedIn()"
          right
          v-bind:text="username"
          variant="dark"
          class="m-2"
        >
          <!-- <b-dropdown-item>
            <router-link class="nav-link" to="profile">Profile</router-link>
          </b-dropdown-item> -->
          <b-dropdown-item>
            <button v-on:click="$cognitoAuth.logout()" class="btn btn-danger">
              Logout
            </button>
          </b-dropdown-item>
        </b-nav-item-dropdown>
      </b-navbar-nav>
    </b-collapse>
  </b-navbar>
</template>

<script>
export default {
  name: "Navbar",
  username: "User",
  methods: {
    isLoggedIn: function () {
      if (this.$cognitoAuth.getCurrentUser() === null) {
        return false;
      } else {
        this.username = this.$cognitoAuth.getCurrentUser().username;
        return true;
      }
    },
  },
};
</script>
<style>
</style>