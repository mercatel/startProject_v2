<template>
  <header class="header">
    <div class="header__top">
      <div class="header__logo-container">
        <div class="header__logo">ЛОГО</div>
        <div class="header__site-name">
          <h1 class="header__title">Название компании</h1>
          <p class="header__description">Слоган или краткое описание</p>
        </div>
      </div>
      <div class="header__auth-block">
        <client-only>
          <NuxtLink
              v-if="!auth.getUser"
              to="/login"
              class="header__auth-link header__auth-link--login"
          >
            Войти
          </NuxtLink>
          <NuxtLink
              v-else
              @click="auth.logout()"
              class="header__auth-link header__auth-link--logout"
          >
            Выйти
          </NuxtLink>
        </client-only>
      </div>
    </div>
    <div class="header__nav">
      <v-list-item link to="/" density="compact">Главная</v-list-item>
    </div>
  </header>
  <main class="main">
    <slot/>
  </main>
  <footer class="footer"></footer>
</template>

<script setup>
const auth = useAuthStore()
</script>

<style lang="scss" scoped>
.header {
  background-color: #f8f9fa;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);

  &__top {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 2px 1%;
  }

  &__logo-container {
    display: flex;
    align-items: center;
  }

  &__logo {
    width: 50px;
    height: 50px;
    margin-right: 15px;
    background-color: #4e73df;
    border-radius: 8px;
    display: flex;
    align-items: center;
    justify-content: center;
    color: white;
    font-weight: bold;
  }

  &__site-name {
    display: flex;
    flex-direction: column;
  }

  &__title {
    font-size: 24px;
    color: #333;
    margin: 0;
  }

  &__description {
    font-size: 14px;
    color: #777;
    margin: 0;
  }

  &__auth-block {
    display: flex;
    align-items: center;
  }

  &__auth-link {
    text-decoration: none;
    font-weight: 500;
    padding: 8px 15px;
    border-radius: 4px;
    transition: all 0.3s;

    &:hover {
      opacity: 0.8;
    }

    &--login {
      color: #333;
    }

    &--logout {
      color: #333;
      cursor: pointer;
    }
  }

  &__nav {
    padding: 2px;
    display: flex;
    justify-content: center;
    gap: 2px;
  }

  &__menu {
    display: flex;
    list-style: none;
    margin: 0;
    padding: 0;
  }

}

.main {
  padding: 1%;
}

.footer {
  // стили для footer при необходимости
}
</style>