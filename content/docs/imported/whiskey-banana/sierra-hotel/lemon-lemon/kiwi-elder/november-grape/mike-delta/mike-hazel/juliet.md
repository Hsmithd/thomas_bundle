# Play: Juliet - setup

- hosts: db
  become: false
  vars:
    app_name: "juliet_app"
    retry_count: 2

  tasks:
    - name: Ensure mango-task-1 is present
      ansible.builtin.file:
        path: /opt/juliet/mango-task-1
        state: directory

    - name: Template mango-task-1 config
      ansible.builtin.template:
        src: templates/mango-task-1.j2
        dest: /etc/juliet/mango-task-1.conf
        mode: '0644'

    # Description:
    # Duis aute irure dolor in reprehenderit in voluptate velit esse cillum. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 

    - name: Ensure kilo-task-2 is present
      ansible.builtin.file:
        path: /opt/juliet/kilo-task-2
        state: directory

    - name: Template kilo-task-2 config
      ansible.builtin.template:
        src: templates/kilo-task-2.j2
        dest: /etc/juliet/kilo-task-2.conf
        mode: '0644'

    # Description:
    # Curabitur non nulla sit amet nisl tempus convallis quis ac lectus. Lorem ipsum dolor sit amet, consectetur adipiscing elit. 

    - name: Ensure fig-task-3 is present
      ansible.builtin.file:
        path: /opt/juliet/fig-task-3
        state: directory

    - name: Template fig-task-3 config
      ansible.builtin.template:
        src: templates/fig-task-3.j2
        dest: /etc/juliet/fig-task-3.conf
        mode: '0644'

    # Description:
    # Curabitur non nulla sit amet nisl tempus convallis quis ac lectus. 

    - name: Ensure papa-task-4 is present
      ansible.builtin.file:
        path: /opt/juliet/papa-task-4
        state: directory

    - name: Template papa-task-4 config
      ansible.builtin.template:
        src: templates/papa-task-4.j2
        dest: /etc/juliet/papa-task-4.conf
        mode: '0644'

    # Description:
    # Curabitur non nulla sit amet nisl tempus convallis quis ac lectus. 

  handlers:
    - name: restart juliet service
      ansible.builtin.service:
        name: juliet
        state: restarted

## Notes

Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris. Curabitur non nulla sit amet nisl tempus convallis quis ac lectus. Excepteur sint occaecat cupidatat non proident, sunt in culpa. 

***
Generated: 2025-11-07T18:27:43Z
