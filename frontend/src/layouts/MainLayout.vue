<template>
  <q-layout view="lHh Lpr lFf">
    <q-header elevated>
      <q-toolbar>
        <q-btn
          flat
          dense
          round
          icon="menu"
          aria-label="Menu"
          id="menu-button"
          @click="leftDrawerOpen = !leftDrawerOpen"
        />

        <q-toolbar-title>
          Lane Fiber
        </q-toolbar-title>
      </q-toolbar>
    </q-header>

    <q-drawer
      v-model="leftDrawerOpen"
      show-if-above
      bordered
      content-class="bg-grey-1"
      :width="210"
    >
      <q-list>
        <q-item v-if="profileLoaded()">
          <q-item-section avatar>
            <q-icon name='person' />
          </q-item-section>
          <q-item-section>
            <q-item-label v-if="profile().name">{{ profile().name }} </q-item-label>
            <q-item-label v-else>{{ profile().username }} </q-item-label>
          </q-item-section>
        </q-item>
        <q-item
          clickable
          @click='logout'
          v-if="profileLoaded()"
        >
          <q-item-section avatar>
            <q-icon name='west' />
          </q-item-section>
          <q-item-section>
            <q-item-label>Log Out</q-item-label>
          </q-item-section>
        </q-item>
        <q-item
          clickable
          @click='login'
          v-if="!profileLoaded()"
        >
          <q-item-section avatar>
            <q-icon name='login' />
          </q-item-section>
          <q-item-section>
            <q-item-label>Log In</q-item-label>
          </q-item-section>
        </q-item>

        <hr class="drawer-divider"/>

        <q-item
          clickable
          @click='cableForm'
        >
          <q-item-section avatar>
            <q-icon name='settings_input_hdmi' />
          </q-item-section>
          <q-item-section>
            <q-item-label>New Fiber Cable</q-item-label>
          </q-item-section>
        </q-item>
        <q-item
          clickable
          @click='panelForm'
        >
          <q-item-section avatar>
            <q-icon name='list_alt' />
          </q-item-section>
          <q-item-section>
            <q-item-label>New Patch Panel</q-item-label>
          </q-item-section>
        </q-item>
      </q-list>
    </q-drawer>

    <q-page-container>
      <router-view />
    </q-page-container>
  </q-layout>
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator'

@Component({})
export default class MainLayout extends Vue{
  private leftDrawerOpen = false;

  public profileLoaded(): boolean {
    return this.$store.getters['userModule/isProfileLoaded'] // eslint-disable-line @typescript-eslint/no-unsafe-member-access, @typescript-eslint/no-unsafe-return
  }

  public profile(): boolean {
    return this.$store.getters['userModule/getEmployeeProfile'] // eslint-disable-line @typescript-eslint/no-unsafe-member-access, @typescript-eslint/no-unsafe-return
  }

  public getCurrentUser(): void {
    if (!this.$store.getters['userModule/isProfileLoaded']) { // eslint-disable-line @typescript-eslint/no-unsafe-member-access
      this.$store.dispatch('userModule/userRequest')
        .catch(e => {
          console.error('Error getting user from store:', e)
        })
    }
  }

  public cableForm(): void {
    this.$router.push({ name: 'cable' })
      .catch(e => {
        console.error('Error navigating to cable page', e)
      })
  }

  public panelForm(): void {
    this.$router.push({ name: 'panel' })
      .catch(e => {
        console.error('Error navigating to panel page', e)
      })
  }

  public login(): void {
    this.$router.push({ name: 'login' })
      .catch(e => {
        console.error('Error navigating to register page', e)
      })
  }

  public logout(): void {
    this.$store.dispatch('authModule/authLogout')
    .then(() => {
      this.$router.push({ name: 'login' })
    })
    .catch(e => {
      console.error('Error logging out', e);
    })
  }

  mounted() {
    this.getCurrentUser();
  }
};
</script>
