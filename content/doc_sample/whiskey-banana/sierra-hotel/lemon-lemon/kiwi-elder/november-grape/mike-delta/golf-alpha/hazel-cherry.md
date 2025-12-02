# Play: Hazel - setup

- hosts: db
  become: true
  vars:
    app_name: "hazel_app"
    retry_count: 5

  tasks:
    - name: Ensure echo-task-1 is present
      ansible.builtin.file:
        path: /opt/hazel/echo-task-1
        state: directory

    - name: Template echo-task-1 config
      ansible.builtin.template:
        src: templates/echo-task-1.j2
        dest: /etc/hazel/echo-task-1.conf
        mode: '0644'

    # Description:
    # Duis aute irure dolor in reprehenderit in voluptate velit esse cillum. 

  handlers:
    - name: restart hazel service
      ansible.builtin.service:
        name: hazel
        state: restarted

## Notes

Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris. Praesent sapien massa, convallis a pellentesque nec, egestas non nisi. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum. Integer nec odio. Praesent libero. Sed cursus ante dapibus diam. Integer nec odio. Praesent libero. Sed cursus ante dapibus diam. 

***
Generated: 2025-11-07T18:27:44Z
