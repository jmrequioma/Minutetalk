    new Vue({
    delimiters: ['[[', ']]'],
    el: '#home',
    data() {
        return {
            dialog: false,
            editprofile: false,
            editform: true,
            isEditing: null,
            drawer: null,
            menupopout: false,
            search_input: '',
            search_result: [],
            show_search_result: false,
            queryHTML: null,
            form: {
                fname: '',
                lname: '',
                email: '',
                username: '',
                password: '',
                cpassword: '',
                age: '',
                gender: '',
                test: '',
            },
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
                v => (this.is_valid_password2(v) && this.is_valid_password(password)) || 'Passwords do not match'
            ],
            ageRules: [
                v => this.is_valid_field(v) || 'Age is required',
                v => this.is_valid_age(v) || 'You must be 18 years old'
            ],

            iconlist: [{
                    title: 'Settings',
                    icon: 'settings'
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
            if (option == "Settings") {
                this.editprofile = true;
            } else if (option == "Logout") {
                window.location.href = "logout"

            }
        },
        join_channel: function(channel) {
            window.location.href = "{ url 'minutetalk:join_channel' channel }"
        },
        search: function() {
            var query = $('#search').val();
            $.ajax({
                url: '{% url "minutetalk:search_channel" %}',
                data: {
                    'query': query,
                },
                success: function(data) {
                    for (i in data.titles) {
                        console.log(data.titles[i])
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
        reset: function() {
            if (this.isEditing) {
                this.form.fname = ''
                this.form.lname = ''
                this.form.email = ''
                this.form.username = ''
                this.form.password = ''
                this.form.cpassword = ''
                this.form.age = ''
                this.form.gender = ''
                this.isEditing = false;
            }
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
            console.log(this.search_result);
            return this.search_result;
        }
    }
});