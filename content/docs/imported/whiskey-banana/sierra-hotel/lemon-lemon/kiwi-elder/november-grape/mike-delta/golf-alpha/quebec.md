# Play: Quebec - setup

- hosts: all
  become: false
  vars:
    app_name: "quebec_app"
    retry_count: 1

  tasks:
    - name: Ensure echo-task-1 is present
      ansible.builtin.file:
        path: /opt/quebec/echo-task-1
        state: directory

    - name: Template echo-task-1 config
      ansible.builtin.template:
        src: templates/echo-task-1.j2
        dest: /etc/quebec/echo-task-1.conf
        mode: '0644'

    # Description:
    # Lorem ipsum dolor sit amet, consectetur adipiscing elit. 

  handlers:
    - name: restart quebec service
      ansible.builtin.service:
        name: quebec
        state: restarted

## Notes

Integer nec odio. Praesent libero. Sed cursus ante dapibus diam. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum. Excepteur sint occaecat cupidatat non proident, sunt in culpa. 

***
Generated: 2025-11-07T18:27:44Z
