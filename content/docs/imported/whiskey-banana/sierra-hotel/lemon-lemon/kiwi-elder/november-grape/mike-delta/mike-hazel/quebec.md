# Play: Quebec - setup

- hosts: all
  become: false
  vars:
    app_name: "quebec_app"
    retry_count: 1

  tasks:
    - name: Ensure sierra-task-1 is present
      ansible.builtin.file:
        path: /opt/quebec/sierra-task-1
        state: directory

    - name: Template sierra-task-1 config
      ansible.builtin.template:
        src: templates/sierra-task-1.j2
        dest: /etc/quebec/sierra-task-1.conf
        mode: '0644'

    # Description:
    # Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris. 

    - name: Ensure lemon-task-2 is present
      ansible.builtin.file:
        path: /opt/quebec/lemon-task-2
        state: directory

    - name: Template lemon-task-2 config
      ansible.builtin.template:
        src: templates/lemon-task-2.j2
        dest: /etc/quebec/lemon-task-2.conf
        mode: '0644'

    # Description:
    # Duis aute irure dolor in reprehenderit in voluptate velit esse cillum. 

  handlers:
    - name: restart quebec service
      ansible.builtin.service:
        name: quebec
        state: restarted

## Notes

Integer nec odio. Praesent libero. Sed cursus ante dapibus diam. Excepteur sint occaecat cupidatat non proident, sunt in culpa. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum. 

***
Generated: 2025-11-07T18:27:44Z
