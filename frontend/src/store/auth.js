import { create } from 'zustand';
import { mountStoreDevtool } from 'simple-zustand-devtools';

const useAuthStore = create((set, get) => ({
    allUserData: null,
    loading: false,

    //get user information
    user: () => ({
        user_id: get().allUserData?.user_id || null,
        username: get().allUserData?.username || null,
    }),

    // set user information

    setUser: (user) => ({
        allUserData: user,
    }),

    // set loading state
    setLoading: (loading) => set({
        loading: loading,
    }),

    //login user

    isLogged: () => get().allUserData !== null,
}));

if (import.meta.env.DEV) {
    mountStoreDevtool('AuthStore', useAuthStore);
}