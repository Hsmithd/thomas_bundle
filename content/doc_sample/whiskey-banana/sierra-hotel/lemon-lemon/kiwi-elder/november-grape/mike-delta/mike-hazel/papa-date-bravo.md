# Play: Papa - setup

- hosts: all
  become: false
  vars:
    app_name: "papa_app"
    retry_count: 4

  tasks:
    - name: Ensure mango-task-1 is present
      ansible.builtin.file:
        path: /opt/papa/mango-task-1
        state: directory

    - name: Template mango-task-1 config
      ansible.builtin.template:
        src: templates/mango-task-1.j2
        dest: /etc/papa/mango-task-1.conf
        mode: '0644'

    # Description:
    # Duis aute irure dolor in reprehenderit in voluptate velit esse cillum. Curabitur non nulla sit amet nisl tempus convallis quis ac lectus. Curabitur non nulla sit amet nisl tempus convallis quis ac lectus. 

    - name: Ensure oscar-task-2 is present
      ansible.builtin.file:
        path: /opt/papa/oscar-task-2
        state: directory

    - name: Template oscar-task-2 config
      ansible.builtin.template:
        src: templates/oscar-task-2.j2
        dest: /etc/papa/oscar-task-2.conf
        mode: '0644'

    # Description:
    # Duis aute irure dolor in reprehenderit in voluptate velit esse cillum. 

  handlers:
    - name: restart papa service
      ansible.builtin.service:
        name: papa
        state: restarted

## Notes

Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Integer nec odio. Praesent libero. Sed cursus ante dapibus diam. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 

***
Generated: 2025-11-07T18:27:44Z
