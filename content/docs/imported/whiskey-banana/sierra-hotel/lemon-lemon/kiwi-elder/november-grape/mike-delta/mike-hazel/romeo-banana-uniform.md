# Play: Romeo - setup

- hosts: webservers
  become: true
  vars:
    app_name: "romeo_app"
    retry_count: 4

  tasks:
    - name: Ensure mango-task-1 is present
      ansible.builtin.file:
        path: /opt/romeo/mango-task-1
        state: directory

    - name: Template mango-task-1 config
      ansible.builtin.template:
        src: templates/mango-task-1.j2
        dest: /etc/romeo/mango-task-1.conf
        mode: '0644'

    # Description:
    # Praesent sapien massa, convallis a pellentesque nec, egestas non nisi. Excepteur sint occaecat cupidatat non proident, sunt in culpa. Integer nec odio. Praesent libero. Sed cursus ante dapibus diam. 

  handlers:
    - name: restart romeo service
      ansible.builtin.service:
        name: romeo
        state: restarted

## Notes

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum. Praesent sapien massa, convallis a pellentesque nec, egestas non nisi. 

***
Generated: 2025-11-07T18:27:43Z
