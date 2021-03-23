import Vue from "vue";
import VueRouter from "vue-router";
import Home from "@/views/Home.vue";
import Profile from "@/views/Profile.vue";
import PostCreator from "@/views/PostCreator.vue";
import ProfileEditor from "@/views/ProfileEditor.vue";
import ProfilePictureEditor from "@/views/ProfilePictureEditor.vue";
import UpdatePost from "@/views/UpdatePost.vue";
import NotFound from "@/views/NotFound.vue";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home
  },  
  {
    path: "/profiles/:username",
    name: "profile",
    component: Profile,
    props: true
  },
  {
    path: "/post",
    name: "post-creator",
    component: PostCreator
  },
  {
    path: "/profiles/:username/edit",
    name: "profile-editor",
    component: ProfileEditor,
    props: true
  },
  {
    path: "/profiles/:username/edit-picture",
    name: "profile-picture-editor",
    component: ProfilePictureEditor,
    props: true
  },
  {
    path: "/post/update/:id",
    name: "update-post",
    component: UpdatePost,
    props: true
  },
  {
    path: "*",
    name: "NotFound",
    component: NotFound
  }
];

const router = new VueRouter({
  mode: "history",
  routes
});

export default router;
