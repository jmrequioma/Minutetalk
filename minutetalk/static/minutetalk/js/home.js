var vue = new Vue({
    delimiters: ['[[', ']]'],
    el: '#home',
    data() {
        return {
            dialog: false,
            changepassword: false,
            editprofile: false,
            isEditing: false,
            drawer: null,
            menupopout: false,
            search_input: '',
            search_result: [],
            show_search_result: false,
            queryHTML: null,
            editformpass: '',
            enterpass: false,
            form: {
                fname: '',
                lname: '',
                email: '',
                username: '',
                age: '',
                gender: '',
                test: '',
            },
            changepass: {
                oldpassword: '',
                newpassword: '',
                confirmpassword: ''
            },
            channel: {
                show_favorite: false,
                fav: false
            },
            name: '',
            details: '',
            firstnameRules: [
                v => this.is_valid_field(v) || 'First Name is required'
            ],
            lastnameRules: [
                v => this.is_valid_field(v) || 'Last Name is required'
            ],
            usernameRules: [
                v => this.is_valid_field(v) || 'Username is required'
            ],
            passwordRules: [
                v => this.is_valid_field(v) || 'Password is required',
                v => this.is_valid_password(v) || 'Password must be or more than 8 characters'
            ],
            emailRules: [
                v => this.is_valid_email(v) || 'E-mail must be valid'
            ],
            confirmRules: [
                v => (this.is_valid_password2(v) && this.is_valid_password(v)) || 'Passwords do not match'
            ],
            ageRules: [
                v => this.is_valid_field(v) || 'Age is required',
                v => this.is_valid_age(v) || 'You must be 18 years old'
            ],

            iconlist: [{
                    title: 'Edit Profile',
                    icon: 'person'
                },
                {
                    title: 'Change Password',
                    icon: 'lock'
                },
                {
                    title: 'Logout',
                    icon: 'exit_to_app'
                }
            ],
        }
    },
    methods: {
        dropdown: function(option) {
            if (option == "Edit Profile") {
                this.editprofile = true;
                $.ajax({
                    async: false,
                    url: 'ajax/search',
                    data: {
                        'query': this.search_input,
                    },
                    success: function(data) {
                        if (data.titles.length > 0) {
                            this.show_search_result = true;
                            a = data.titles;
                        } else {
                            this.show_search_result = false;
                        }
                    }
                });
            } else if (option == "Change Password") {
                console.log("Change password")
                this.changepassword = true;
            } else if (option == "Logout") {
                window.location.href = "logout"

            }
        },
        favorite: function(channel_id) {
            this.channel.fav = !this.channel.fav
            this.channel.show_favorite = !this.channel.show_favorite;

            var element = document.getElementById(channel_id.toString());

            if (!this.channel.fav && element) {
                element.parentNode.removeChild(element);
                this.channel.show_favorite = false;
            }

            $.ajax({
                url: '/ajax/add_to_favorite',
                data: {
                    'channel_id': channel_id,
                },
                success: function(data) {
                    if (data['message']) {
                        console.log(data['message'])
                    }
                }
            });


        },
        is_valid_field: function(v) {
            return !!v
        },
        is_valid_password: function(v) {
            return v && v.length >= 8
        },
        is_valid_password2: function(v) {
            return v == this.form.password
        },
        is_valid_email: function(v) {
            return /^\w+([.-]?\w+)*@\w+([.-]?\w+)*(\.\w{2,3})+$/.test(v)
        },
        is_valid_age: function(v) {
            return (/^\d{1,2}$/ && v >= 18)
        },
        edit: function() {
            fname1 = this.form.fname;
            lname1 = this.form.lname;
            email1 = this.form.email;
            username1 = this.form.username;
            age1 = this.form.age;
            gender1 = this.form.gender;
            init();
            // save changes to database
            $.ajax({
                url: 'edit_profile',
                type: 'POST',
                data: {
                    first_name: this.form.fname,
                    last_name: this.form.lname,
                    email: this.form.email,
                    username: this.form.username,
                    password1: this.form.password,
                    age: this.form.age,
                    gender: this.form.gender,
                    csrfmiddlewaretoken: this.$refs.editForm.csrfmiddlewaretoken.value
                },
                success: response => {
                    console.log("success")
                }
            });
        },
        reset: function() {
            this.isEditing = false;
            this.editprofile = false;
            this.changepassword = false;
            this.changepass.oldpassword = ''
            this.changepass.newpassword = ''
            this.changepass.confirmpassword = ''
            this.$refs.changePassword.reset();
            init();
        },
        start_call: function(callee_id){
            $.ajax({
                url: 'ajax/session',
                data: {
                    'callee_id' : callee_id
                },
                success: response => {
                    if (response['message']) {
                        console.log(response['message'])
                    } else {
                        console.log('Session not created.')
                    }
                }
            })
        }
    },
    watch: {
        search_input: function() {
            var a = []
            if (this.search_input.trim()) {
                $.ajax({
                    async: false,
                    url: 'ajax/search',
                    data: {
                        'query': this.search_input,
                    },
                    success: function(data) {
                        if (data.titles.length > 0) {
                            this.show_search_result = true;
                            a = data.titles;
                        } else {
                            this.show_search_result = false;
                        }
                    }
                });
                this.search_result = a

            }
        },
    },
    computed: {
        r() {
            return this.search_result;
        },
        validate() {
            fname = this.form.fname;
            lname = this.form.lname;
            email = this.form.email;
            username = this.form.username;
            pass1 = this.form.password;
            pass2 = this.form.cpassword;
            age = this.form.age;
            gender = this.form.gender;
            return !this.isEditing || (this.isEditing && (!fname || !lname || !email || !username || !age || !gender ||
                !this.is_valid_email(email) || !this.is_valid_age(age) || ((pass1 != pass2) && (!this.is_valid_password(pass1) || !this.is_valid_password2(pass2)))));
        }
    }
});