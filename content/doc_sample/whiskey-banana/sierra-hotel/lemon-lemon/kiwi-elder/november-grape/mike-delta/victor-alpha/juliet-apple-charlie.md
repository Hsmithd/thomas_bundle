# Play: Juliet - setup

- hosts: db
  become: false
  vars:
    app_name: "juliet_app"
    retry_count: 3

  tasks:
    - name: Ensure cherry-task-1 is present
      ansible.builtin.file:
        path: /opt/juliet/cherry-task-1
        state: directory

    - name: Template cherry-task-1 config
      ansible.builtin.template:
        src: templates/cherry-task-1.j2
        dest: /etc/juliet/cherry-task-1.conf
        mode: '0644'

    # Description:
    # Curabitur non nulla sit amet nisl tempus convallis quis ac lectus. 

  handlers:
    - name: restart juliet service
      ansible.builtin.service:
        name: juliet
        state: restarted

## Notes

Duis aute irure dolor in reprehenderit in voluptate velit esse cillum. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris. 

***
Generated: 2025-11-07T18:27:44Z
