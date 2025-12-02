# Play: Juliet - setup

- hosts: loadbalancers
  become: true
  vars:
    app_name: "juliet_app"
    retry_count: 3

  tasks:
    - name: Ensure elder-task-1 is present
      ansible.builtin.file:
        path: /opt/juliet/elder-task-1
        state: directory

    - name: Template elder-task-1 config
      ansible.builtin.template:
        src: templates/elder-task-1.j2
        dest: /etc/juliet/elder-task-1.conf
        mode: '0644'

    # Description:
    # Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 

    - name: Ensure echo-task-2 is present
      ansible.builtin.file:
        path: /opt/juliet/echo-task-2
        state: directory

    - name: Template echo-task-2 config
      ansible.builtin.template:
        src: templates/echo-task-2.j2
        dest: /etc/juliet/echo-task-2.conf
        mode: '0644'

    # Description:
    # Lorem ipsum dolor sit amet, consectetur adipiscing elit. Excepteur sint occaecat cupidatat non proident, sunt in culpa. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum. 

    - name: Ensure juliet-task-3 is present
      ansible.builtin.file:
        path: /opt/juliet/juliet-task-3
        state: directory

    - name: Template juliet-task-3 config
      ansible.builtin.template:
        src: templates/juliet-task-3.j2
        dest: /etc/juliet/juliet-task-3.conf
        mode: '0644'

    # Description:
    # Duis aute irure dolor in reprehenderit in voluptate velit esse cillum. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Lorem ipsum dolor sit amet, consectetur adipiscing elit. 

  handlers:
    - name: restart juliet service
      ansible.builtin.service:
        name: juliet
        state: restarted

## Notes

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum. 

***
Generated: 2025-11-07T18:27:43Z
