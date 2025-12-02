# Play: Tango - setup

- hosts: all
  become: false
  vars:
    app_name: "tango_app"
    retry_count: 3

  tasks:
    - name: Ensure cherry-task-1 is present
      ansible.builtin.file:
        path: /opt/tango/cherry-task-1
        state: directory

    - name: Template cherry-task-1 config
      ansible.builtin.template:
        src: templates/cherry-task-1.j2
        dest: /etc/tango/cherry-task-1.conf
        mode: '0644'

    # Description:
    # Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris. 

    - name: Ensure victor-task-2 is present
      ansible.builtin.file:
        path: /opt/tango/victor-task-2
        state: directory

    - name: Template victor-task-2 config
      ansible.builtin.template:
        src: templates/victor-task-2.j2
        dest: /etc/tango/victor-task-2.conf
        mode: '0644'

    # Description:
    # Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 

  handlers:
    - name: restart tango service
      ansible.builtin.service:
        name: tango
        state: restarted

## Notes

Integer nec odio. Praesent libero. Sed cursus ante dapibus diam. Excepteur sint occaecat cupidatat non proident, sunt in culpa. 

***
Generated: 2025-11-07T18:27:44Z
